// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
    site: 'https://sungil-i.github.io',
    vite: {
        server: {
            watch: {
                usePolling: true,
                interval: 100, // 원준님이 말씀하신 100ms 주기로 파일을 감시합니다.
            },
        },
    },
    markdown: {
        shikiConfig: {
            // 단일 theme 속성 대신 themes 객체를 사용하여 두 가지 테마를 지정합니다.
            themes: {
                light: 'github-light',
                dark: 'github-dark',
            },
            // 긴 코드의 가로 스크롤을 방지하고 줄바꿈을 원하시면 true로 설정하세요.
            wrap: false,
        },
    },
});
