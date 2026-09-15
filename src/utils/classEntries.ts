// src/utils/classEntries.ts
// YearSelector와 MainLayout이 동일한 수업 목록을 공유하기 위한 유틸리티입니다.
import fs from "fs";
import path from "path";

const pagesRoot = path.resolve("./src/pages");
// 학년도 폴더만 허용합니다 (4자리 숫자). `upj53` 등 비공개/비학년도 폴더는
// 이 패턴에 걸리지 않으므로 학생용 드롭다운에 자동으로 노출되지 않습니다.
const YEAR_FOLDER_PATTERN = /^\d{4}$/;

export interface ClassEntry {
  year: string;
  folder: string;
  value: string;
  label: string;
}

export function getClassEntries(): ClassEntry[] {
  const classEntries: ClassEntry[] = [];

  if (!fs.existsSync(pagesRoot)) {
    return classEntries;
  }

  const years = fs
    .readdirSync(pagesRoot, { withFileTypes: true })
    .filter(
      (dirent) => dirent.isDirectory() && YEAR_FOLDER_PATTERN.test(dirent.name),
    )
    .map((dirent) => dirent.name);

  for (const year of years) {
    const yearDir = path.join(pagesRoot, year);
    const subfolders = fs
      .readdirSync(yearDir, { withFileTypes: true })
      .filter((dirent) => dirent.isDirectory())
      .map((dirent) => dirent.name);

    for (const folder of subfolders) {
      classEntries.push({
        year,
        folder,
        value: `/${year}/${folder}/`,
        label: `${year}년 : ${folder}`,
      });
    }
  }

  // 최신 글이 위로 오도록 연도, 폴더명 역순으로 정렬합니다.
  classEntries.sort((a, b) => {
    if (a.year !== b.year) return b.year.localeCompare(a.year);
    return b.folder.localeCompare(a.folder);
  });

  return classEntries;
}
