# core/symbol_mapper.py
from enum import Enum
import logging
from typing import Optional

logger = logging.getLogger(__name__)

# 1. Type Safety 확보를 위한 계좌 타입 Enum 정의
class MT5AccountType(str, Enum):
    STP = "STP"
    DEMO = "DEMO"
    ECN = "ECN"
    WON = "WON"

# ✨ core/config.py가 DEMO_1(Scalping 전담)/DEMO_2(Swing 전담)
# 두 개의 물리 데모 계좌를 관리하게 되었지만, 이 파일의 MT5AccountType은 여전히 "업무적
# 계좌 분류"(수수료 모델/심볼 접미사 기준) 축이지 "물리 계좌" 축이 아니다. 두 데모 계좌
# 모두 config.py의 _load_mt5_profile()에서 account_type="DEMO"로 귀결되므로(DEMO_2는
# MT5_ACCOUNT_TYPE_DEMO_2가 .env에 없어 "DEMO"로 폴백됨), 아래 MT5_TICKER_MAP /
# COMMISSION_PER_LOT_USD / ACCOUNT_FEE_MODELS의 기존 MT5AccountType.DEMO 항목이 DEMO_1과
# DEMO_2 모두에 그대로 재사용된다 - 구조 변경이 필요 없다.
# 위 에서 flag했던 "DEMO_2가 WON과 동일한 Hantec Markets
# 터미널 폴더를 쓴다"는 우려는 해소되었다: `.env`의 실제 로그인 서버는 두 계좌 모두
# `MT5_SERVER_NAME_DEMO_1`/`MT5_SERVER_NAME_DEMO_2` = "InfinoxLimited-MT5Demo"로 완전히
# 동일하다 - `MT5_TERMINAL_PATH_DEMO_2`가 가리키는 "Hantec Markets MetaTrader 5" 폴더는
# 그저 재사용된 터미널 실행파일 설치 위치일 뿐, 실제 로그인 브로커/서버는 DEMO_1과 같은
# Infinox이다. 따라서 DEMO_1/DEMO_2 모두 아래의 접미사 없는 MT5AccountType.DEMO 심볼
# 딕셔너리({"XAUUSD": "XAUUSD", "NAS100": "NAS100", "EURUSD": "EURUSD", "USOUSD": "USOUSD"})를
# 그대로 공유하는 것이 맞다 - 별도 심볼 분기나 접미사 처리가 불필요하다.
# 2. 심볼 맵핑 레지스트리 (Dictionary)
MT5_TICKER_MAP = {
    MT5AccountType.STP:  {"XAUUSD": "XAUUSD",  "NAS100": "NAS100",  "EURUSD": "EURUSD",  "USOUSD": "USOUSD", "BTCUSD": "BTCUSD"},
    MT5AccountType.DEMO: {"XAUUSD": "XAUUSD",  "NAS100": "NAS100",  "EURUSD": "EURUSD",  "USOUSD": "USOUSD", "BTCUSD": "BTCUSD"},
    MT5AccountType.ECN:  {"XAUUSD": "XAUUSD+", "NAS100": "NAS100+", "EURUSD": "EURUSD+", "USOUSD": "USOUSD+", "BTCUSD": "BTCUSD.a"},
    MT5AccountType.WON:  {"XAUUSD": "XAUUSD",  "NAS100": "US100.x", "EURUSD": "EURUSD",  "USOUSD": "USOIL+", "BTCUSD": "BTCUSD"},
}

# 3. 계좌별 과금 방식 분류
# ReportHistory(2026-07-20-b) 실측 결과: 계좌마다 수수료를 직접 차감하는지(Per-lot Commission),
# 혹은 스프레드를 넓혀 비용을 숨기는지(Spread-markup) 과금 모델이 다르다.
class FeeModel(str, Enum):
    SPREAD_MARKUP = "SPREAD_MARKUP"          # 명시적 커미션 없음 (스프레드에 비용 내재)
    PER_LOT_COMMISSION = "PER_LOT_COMMISSION"  # 체결 시 랏당 고정 커미션을 직접 차감

ACCOUNT_FEE_MODELS = {
    MT5AccountType.DEMO: FeeModel.SPREAD_MARKUP,
    MT5AccountType.STP:  FeeModel.SPREAD_MARKUP,
    MT5AccountType.ECN:  FeeModel.PER_LOT_COMMISSION,
    MT5AccountType.WON:  FeeModel.PER_LOT_COMMISSION,
}

# 4. 계좌별 x 티커별 1랏 거래당 실측 수수료 (USD 단위)
# trading_results/2026-07-20-b 의 ReportHistory-*.xlsx 를 0.01랏/1.0랏 두 실측치로 교차 검증하여 산출.
# [주의] STP는 ACCOUNT_FEE_MODELS 상 SPREAD_MARKUP으로 분류되지만, NAS100 한 종목에 한해
# 실측 커미션이 0이 아닌 -0.7 USD/lot로 확인되었다(브로커가 지수 상품에만 예외적으로 소액 커미션을
# 추가로 부과하는 케이스). PnL 시뮬레이터 정확도를 위해 이 예외치는 0으로 뭉개지 않고 그대로 반영한다.
COMMISSION_PER_LOT_USD = {
    MT5AccountType.DEMO: {"XAUUSD": 0.0,  "NAS100": 0.0, "EURUSD": 0.0,  "USOUSD": 0.0},
    MT5AccountType.STP:  {"XAUUSD": 0.0,  "NAS100": 0.7, "EURUSD": 0.0,  "USOUSD": 0.0},
    MT5AccountType.ECN:  {"XAUUSD": 15.0, "NAS100": 0.7, "EURUSD": 15.0, "USOUSD": 2.0},
    MT5AccountType.WON:  {"XAUUSD": 15.0, "NAS100": 6.0, "EURUSD": 15.0, "USOUSD": 2.0},
}

# 5. 헷지 마진(Hedged Margin) 정책
# 의 1.0랏 BUY+SELL 동시 스트레스 테스트에서 4개 계좌 전부 NO_MONEY 없이 체결된 것으로
# 실측 확인됨: 브로커가 방향성이 상쇄된 포지션의 필요 증거금을 100% 합산하지 않고 0에 가깝게
# 상계(Netting) 처리하는 정책을 사용 중임을 의미한다.
HEDGING_MARGIN_POLICY = "NETTING_TO_ZERO"

def get_mt5_ticker(tv_symbol: str, account_type_str: str) -> str:
    """
    TradingView에서 전달받은 범용 심볼을 해당 계좌 타입에 맞는 MT5 전용 심볼로 변환합니다.
    """
    # 1. 문자열을 Enum 객체로 안전하게 변환 (오타 및 예외 방어)
    try:
        account_type = MT5AccountType(account_type_str.upper())
    except ValueError:
        logger.error(f"❌ [SymbolMapper] 등록되지 않은 계좌 타입입니다: {account_type_str}. 기본 심볼을 반환합니다.")
        return tv_symbol

    # 2. 맵핑 테이블 조회
    account_map = MT5_TICKER_MAP.get(account_type, {})
    mt5_symbol = account_map.get(tv_symbol.upper())

    # 3. 맵핑 테이블에 정의되지 않은 종목이 들어올 경우 원본(TV 심볼) 그대로 반환 (Fallback)
    if not mt5_symbol:
        logger.warning(f"⚠️ [SymbolMapper] '{account_type.value}' 계좌에 '{tv_symbol}' 맵핑이 없습니다. 원본을 유지합니다.")
        return tv_symbol

    return mt5_symbol


# ✨ Requirement 06(2026-07-26): PineScript는 계좌 타입 짧은 코드("ECN")가 아니라
# server_type 전체 문자열("MT5_SERVER_NAME_ECN")을 보낸다. get_mt5_ticker()는 이미
# 짧은 코드를 받는 용도로 다른 호출부(modules/trade_worker.py 등)가 쓰고 있으므로
# 기존 함수를 건드리지 않고, server_type 파싱 책임만 지는 별도 함수를 추가한다.
_MT5_SERVER_NAME_PREFIX = "MT5_SERVER_NAME_"


def get_mt5_ticker_from_server_type(tv_ticker: str, server_type: str) -> Optional[str]:
    """
    웹훅 원본 필드 그대로(raw ticker="XAUUSD" 등, raw server_type="MT5_SERVER_NAME_ECN" 등)를
    받아 MT5 전용 심볼("XAUUSD+" 등)을 반환합니다.

    get_mt5_ticker()와 달리 맵핑에 실패하면 원본을 그대로 반환(Fallback)하지 않고 None을
    반환합니다 - 호출부(main.py)가 "매핑 실패 시 MT5 실행 로직만 안전하게 건너뛴다"는
    Requirement 06 Task 3 요구사항을 명확히 구현할 수 있도록, 실패를 숨기지 않고 신호로
    노출하기 위함입니다(DB 원본 로그 저장은 이 함수 호출 이전에 이미 끝나 있어야 합니다).
    """
    # 🛡️ [Whitespace & Case Trimming] TradingView/PineScript 전송 경로에서 섞여 들어올 수
    # 있는 앞뒤 공백이나 대소문자 표기 차이("mt5_server_name_ecn " 등)로 인한 "String
    # Matching Gap"을 원천 차단한다.
    normalized_server_type = server_type.strip().upper()
    if not normalized_server_type.startswith(_MT5_SERVER_NAME_PREFIX):
        logger.warning(f"⚠️ [SymbolMapper] server_type 형식이 올바르지 않습니다: {server_type!r}. MT5 실행을 건너뜁니다.")
        return None
    account_type_str = normalized_server_type[len(_MT5_SERVER_NAME_PREFIX):]

    normalized_ticker = tv_ticker.strip().upper()
    if normalized_ticker == "UNKNOWN":
        logger.warning(f"⚠️ [SymbolMapper] ticker가 UNKNOWN입니다(원본 server_type={server_type!r}). MT5 실행을 건너뜁니다.")
        return None

    try:
        account_type = MT5AccountType(account_type_str)
    except ValueError:
        logger.warning(f"⚠️ [SymbolMapper] 등록되지 않은 계좌 타입입니다: server_type={server_type!r}(파싱={account_type_str!r}). MT5 실행을 건너뜁니다.")
        return None

    account_map = MT5_TICKER_MAP.get(account_type, {})
    mt5_symbol = account_map.get(normalized_ticker)
    if not mt5_symbol:
        logger.warning(f"⚠️ [SymbolMapper] '{account_type.value}' 계좌에 '{normalized_ticker}' 맵핑이 없습니다. MT5 실행을 건너뜁니다.")
        return None

    return mt5_symbol


# 6. 브로커 심볼별 거래량(Volume) 스펙 - Min/Max/Step
# ✨ [my_strategy_v2 Requirement 21, 2026-08-06] 브로커가 공지한 세 핵심 심볼의 랏 스펙을
# 정적으로 보관한다(계좌 타입과 무관하게 동일 - STP/DEMO/ECN/WON 전부 같은 브로커 심볼
# 스펙을 공유). 위 MT5_TICKER_MAP/COMMISSION_PER_LOT_USD 등 기존 구조는 전혀 건드리지
# 않고 순수 추가(Append-only)만 한다.
MT5_VOLUME_MAP = {
    "XAUUSD": {"min": 0.01, "max": 20, "step": 0.01},
    "USOUSD": {"min": 0.01, "max": 100, "step": 0.01},
    "NAS100": {"min": 0.01, "max": 100, "step": 0.01},
}