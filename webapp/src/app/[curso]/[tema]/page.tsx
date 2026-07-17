import { getTopicBySlug, getCourses, getTopics } from '@/lib/api';
import MarkdownRenderer from '@/components/MarkdownRenderer';
import { notFound } from 'next/navigation';

export async function generateStaticParams() {
  const courses = getCourses();
  const params: { curso: string, tema: string }[] = [];

  for (const curso of courses) {
    const topics = getTopics(curso);
    for (const topic of topics) {
      params.push({
        curso,
        tema: topic.slug,
      });
    }
  }

  return params;
}

export default async function TopicPage({ params }: { params: Promise<{ curso: string, tema: string }> }) {
  const { curso, tema } = await params;
  const topicData = getTopicBySlug(curso, tema);

  if (!topicData) {
    notFound();
  }

  return (
    <div className="glass-card">
      <MarkdownRenderer content={topicData.content} />
    </div>
  );
}
