/** @type {import('tailwindcss').Config} */
module.exports = {
    theme: {
        extend: {
            fontFamily: {
                sans: ['Vazirmatn', 'ui-sans-serif', 'system-ui'],
            },
        },
    },
    plugins: [],
    corePlugins: {
        preflight: true,
    },
    darkMode: 'class',
    direction: 'rtl'
};