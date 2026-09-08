// src/utils/classEntries.ts
// YearSelector와 MainLayout이 동일한 수업 목록을 공유하기 위한 유틸리티입니다.
import fs from "fs";
import path from "path";

const pagesRoot = path.resolve("./src/pages");
const targetYears = ["2025", "2026"];

export interface ClassEntry {
  year: string;
  folder: string;
  value: string;
  label: string;
}

export function getClassEntries(): ClassEntry[] {
  const classEntries: ClassEntry[] = [];

  for (const year of targetYears) {
    const yearDir = path.join(pagesRoot, year);
    if (fs.existsSync(yearDir)) {
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
  }

  // 최신 글이 위로 오도록 연도, 폴더명 역순으로 정렬합니다.
  classEntries.sort((a, b) => {
    if (a.year !== b.year) return b.year.localeCompare(a.year);
    return b.folder.localeCompare(a.folder);
  });

  return classEntries;
}
