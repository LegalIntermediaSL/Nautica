import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const titulacionesDirectory = path.join(process.cwd(), '../titulaciones');

export function getCourses() {
  if (!fs.existsSync(titulacionesDirectory)) {
    return [];
  }
  const courses = fs.readdirSync(titulacionesDirectory)
    .filter(name => fs.statSync(path.join(titulacionesDirectory, name)).isDirectory());
  
  // Sort naturally: PER, PY, CY
  const order = ['PER', 'PY', 'CY'];
  return courses.sort((a, b) => {
    return order.indexOf(a) - order.indexOf(b);
  });
}

export function getTopics(course: string) {
  const courseDir = path.join(titulacionesDirectory, course);
  if (!fs.existsSync(courseDir)) return [];
  
  const files = fs.readdirSync(courseDir).filter(f => f.endsWith('.md'));
  
  const topics = files.map(filename => {
    const slug = filename.replace(/\.md$/, '');
    // Regex to match "tema_1_..."
    const match = slug.match(/tema_(\d+)_(.*)/);
    let name = slug;
    let number = 999;
    if (match) {
      number = parseInt(match[1]);
      name = `Tema ${match[1]}: ${match[2].replace(/_/g, ' ')}`;
      // Capitalize first letters
      name = name.replace(/\b\w/g, c => c.toUpperCase());
    }
    return { slug, name, number };
  });

  return topics.sort((a, b) => a.number - b.number);
}

export function getTopicBySlug(course: string, slug: string) {
  const fullPath = path.join(titulacionesDirectory, course, `${slug}.md`);
  if (!fs.existsSync(fullPath)) return null;

  const fileContents = fs.readFileSync(fullPath, 'utf8');
  const { data, content } = matter(fileContents);

  return {
    slug,
    content,
    ...data,
  };
}
