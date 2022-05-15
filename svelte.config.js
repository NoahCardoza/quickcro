// import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-static';

const dev = process.env.NODE_ENV === 'development';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // preprocess: preprocess(),
  kit: {
    adapter: adapter({
      fallback: ['index.html', 'security.html'],
      precompress: true
    }),
    paths: {
      base: dev && '' || '/quickcro',
    },
    trailingSlash: 'never',
    appDir: 'internal',
  },
};

export default config;
