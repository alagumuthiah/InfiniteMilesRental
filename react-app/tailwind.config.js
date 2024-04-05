/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'dark-blue': '#03045e',
        'custom-blue': '#0077B6',
        'light-blue': '#355070'
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

/*
https://tailwindcss.com/docs/guides/create-react-app
*/
