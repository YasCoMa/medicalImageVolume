export default defineNuxtConfig({
  app: {
    head: {
      title: "Medical Image Processing",
      link: [
        { rel: "icon", type: "image/png", href: "/favicon.ico" },
        { rel: "stylesheet", href: "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900&display=swap" }
      ],
    }
  },

  sourcemap: { client: true },

  imports: {
    dirs: [
      "composables",
    ]
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE,
    }
  },

  modules:[
    "@nuxtjs/tailwindcss",
  ],

  components: [
    "components",
  ],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

});
