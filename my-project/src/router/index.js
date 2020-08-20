import Vue from 'vue';
import Router from 'vue-router';
import ElementUI from 'element-ui';
import CHome from '@/views/Home';
import Blog from '@/views/blog';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'CHome',
      component: CHome
    },
    {
      path: '/blog',
      name: 'Blog',
      component: Blog
    }
  ]
});
