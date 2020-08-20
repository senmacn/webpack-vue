<template>
  <el-container class="s-blog-container">
    <el-aside width="200px">
      <el-menu class="el-menu-vertical blog-aside-menu">
        <el-menu-item index="1">
          <i class="el-icon-s-home"></i>
          <span slot="title">主页</span>
        </el-menu-item>
        <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">功能</span>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-setting"></i>
          <span slot="title">设置</span>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header
        class="s-blog-header"
        height="200px">

      </el-header>
      <el-main height="auto">

      </el-main>
    </el-container>

  </el-container>
</template>

<script>
export default {
  name: 'Blog',
  data () {
    return {
    };
  }
};
</script>

<style>
.s-blog-header {
  background: url('../../assets/images/back1.jpg');
}
.blog-aside-menu {
  background-color: '#545c64';
}
</style>
