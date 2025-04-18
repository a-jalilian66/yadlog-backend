/** @type {import('tailwindcss').Config} */
module.exports = {
    safelist: [
        'code-block',
        'code-block-container',
        'code-wrapper',
        'copy-btn',
        'text-green-400',
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/typography'),
    ],
}