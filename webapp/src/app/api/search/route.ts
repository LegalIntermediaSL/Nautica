import { NextResponse } from 'next/server';
import { getAllSearchableContent } from '@/lib/api';
import Fuse from 'fuse.js';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('q');

  if (!query) {
    return NextResponse.json({ results: [] });
  }

  const allContent = getAllSearchableContent();

  const options = {
    includeScore: true,
    threshold: 0.3,
    keys: [
      { name: 'title', weight: 0.5 },
      { name: 'description', weight: 0.3 },
      { name: 'content', weight: 0.2 }
    ]
  };

  const fuse = new Fuse(allContent, options);
  const searchResults = fuse.search(query);

  // Map results to only send what's necessary to the client (don't send full markdown content)
  const formattedResults = searchResults.map(result => ({
    id: result.item.id,
    course: result.item.course,
    slug: result.item.slug,
    title: result.item.title,
    description: result.item.description,
    score: result.score
  })).slice(0, 10); // Limit to top 10 results

  return NextResponse.json({ results: formattedResults });
}
