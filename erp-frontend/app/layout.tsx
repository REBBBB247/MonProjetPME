import "./globals.css";

export const metadata = {
  title: "ERP App",
  description: "Gestion ERP avec Next.js et TailwindCSS",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body className="bg-gray-100">{children}</body>
    </html>
  );
}
