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
});
