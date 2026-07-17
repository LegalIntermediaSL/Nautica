import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import 'katex/dist/katex.min.css';
import { getCourses, getTopics } from "@/lib/api";

export const metadata: Metadata = {
  title: "Nautica - Enciclopedia",
  description: "Tratado Náutico Universitario (PER, PY, CY)",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const courses = getCourses();

  return (
    <html lang="es">
      <body>
        <nav className="sidebar">
          <h1>Nautica</h1>
          {courses.map(course => (
            <div key={course}>
              <div className="course-title">{course}</div>
              {getTopics(course).map(topic => (
                <Link 
                  href={`/${course}/${topic.slug}`} 
                  key={topic.slug}
                  className="topic-link"
                >
                  {topic.name}
                </Link>
              ))}
            </div>
          ))}
        </nav>
        <main className="main-content">
          {children}
        </main>
      </body>
    </html>
  );
}
