/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./node_modules/@abifa-ui/components/**/*.{js,vue,ts}",
    "./@abifa-ui/components/**/*.{js,vue,ts}",
    "./app.vue",
    "./node_modules/mtw-nuxt-components/components/**/*.{js,vue,ts}"
  ],
  // important: true,
  theme: {
    extend: {
      colors: {
        "primary-200": "#d4e2ee",
        "primary-400": "#51a0e2",
        "primary-500": "#4299e1",
        "primary-600": "#51a0e2",
        "primary-700": "#258be0",
        "primary-800": "#1080de",

        "secondary-500": "#1f2937"
      }
    }
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/aspect-ratio")
  ],
};
