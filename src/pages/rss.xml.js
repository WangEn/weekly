import rss from '@astrojs/rss';

let allPosts = import.meta.glob('./posts/*.md', { eager: true });
let posts = Object.values(allPosts);
posts = posts.sort((a, b) => {
  return (
    parseInt(b.url.split('/posts/')[1].split('-')[0]) -
    parseInt(a.url.split('/posts/')[1].split('-')[0])
  );
});

//只保留15，当前太多了
posts.splice(10);

export const get = () =>
  rss({
    title: '爱情的纹理',
    description: '记录自诩热爱生活的工程师 Warn 的简单生活',
    site: 'https://www.715721.xyz/',
    customData: `<image><url>https://pub-b18af89466c74e8aa9cd24048eedc556.r2.dev/weekly/weekly-icon.png</url></image>`,
    items: posts.map((item) => {
      const url = item.url;
      const oldTitle = url.split('/posts/')[1];
      const title =
        '第' + oldTitle.split('-')[0] + '期 - ' + oldTitle.split('-')[1];
      return {
        link: url,
        title,
        description: item.compiledContent(),
        pubDate: item.frontmatter.date,
      };
    }),
  });
