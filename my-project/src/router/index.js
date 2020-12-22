import Vue from 'vue';
import Router from 'vue-router';
import ElementUI from 'element-ui';
import Blog from '@/views/blog';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/blog'
    },
    {
      path: '/blog',
      name: 'Blog',
      component: Blog
    }
  ]
});
