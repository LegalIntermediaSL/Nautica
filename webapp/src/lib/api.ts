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
  
  // Sort naturally: LN, PNB, PER, PY, CY
  const order = ['LN', 'PNB', 'PER', 'PY', 'CY'];
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

export function getAllSearchableContent() {
  const courses = getCourses();
  const allContent = [];

  for (const course of courses) {
    const topics = getTopics(course);
    for (const topic of topics) {
      const fullPath = path.join(titulacionesDirectory, course, `${topic.slug}.md`);
      if (fs.existsSync(fullPath)) {
        const fileContents = fs.readFileSync(fullPath, 'utf8');
        const { data, content } = matter(fileContents);
        
        allContent.push({
          id: `${course}-${topic.slug}`,
          course,
          slug: topic.slug,
          name: topic.name,
          title: data.title || topic.name,
          description: data.description || '',
          content: content
        });
      }
    }
  }

  return allContent;
}
