<template>
  <el-container class="s-blog-container">
    <el-header
      class="blog-header"
      height="150px"
    >
    </el-header>
    <el-main class="blog-main">
      <el-header class="menu-container">
        <el-menu
        class="blog-menu"
          mode="horizontal"
          default-active="0"
          @select="handleSelectBlogTypes"
        >
            <el-menu-item
              v-for="(item, index) in BLOG_TYPES"
              :index="String(index)"
              :key="index"
            >
              {{item.title}}
            </el-menu-item>
        </el-menu>
      </el-header>
      <el-main class="blog-content">

      </el-main>
    </el-main>
  </el-container>
</template>

<script>
import { BLOG_TYPES } from '../../settings/blogSettings';

export default {
  name: 'Blog',
  data () {
    return {
      BLOG_TYPES
    };
  },
  methods: {
    handleSelectBlogTypes (index) {
      // const type = this.BLOG_TYPES[index.type];
    }
  }
};
</script>

<style>
.s-blog-container {}
.blog-header {
  background: url('../../assets/images/back1.jpg');
  background-size: cover;
}
.blog-main {
  max-width: 1000px;
  min-width: 600px;
  width: 70vw;
  margin: 0 auto;
  margin-top: 20px;
  border: 1px solid black;
}
.blog-menu {
  display: flex;
}
.blog-menu li {
  flex: 1;
}
</style>
