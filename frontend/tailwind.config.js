import frappeUIPreset from "frappe-ui/src/tailwind/preset"

/** @type {import('tailwindcss').Config} */
export default {
  presets: [frappeUIPreset],
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/frappe-ui/src/components/**/*.{vue,js}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#2a7f3e",
          light: "#3d9970",
          dark: "#1a4d2a",
          accent: "#4caf50",
        },
        brand: {
          primary: "#2a7f3e",
          light: "#3d9970",
          dark: "#1a4d2a",
          accent: "#4caf50",
        },
        surface: {
          bg: "#f5f5f5",
          card: "#ffffff",
          "card-hover": "#f9f9f9",
          border: "#e5e7eb",
        },
      },
      boxShadow: {
        "card": "0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)",
        "card-hover": "0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)",
        "btn": "0 4px 6px -1px rgba(42,127,62,0.3)",
      },
      animation: {
        "float": "float 3s ease-in-out infinite",
        "slide-up": "slide-up 0.5s ease-out",
        "hover-lift": "hover-lift 0.3s ease-out forwards",
        "hover-glow": "hover-glow 0.3s ease-out forwards",
        "fade-in-up": "fade-in-up 0.6s ease-out forwards",
      },
      keyframes: {
        "float": {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-10px)" },
        },
        "slide-up": {
          "0%": { opacity: "0", transform: "translateY(20px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        "hover-lift": {
          "0%": { transform: "translateY(0)" },
          "100%": { transform: "translateY(-8px)" },
        },
        "hover-glow": {
          "0%": { boxShadow: "0 4px 6px -1px rgba(0,0,0,0.1)" },
          "100%": { boxShadow: "0 20px 25px -5px rgba(42,127,62,0.15), 0 8px 10px -6px rgba(0,0,0,0.1)" },
        },
        "fade-in-up": {
          "0%": { opacity: "0", transform: "translateY(30px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
      },
    },
  },
  plugins: [],
}
