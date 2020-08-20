<template>
  <el-container class="s-blog-container">
    <el-aside width="200px">
      <el-menu class="el-menu-vertical blog-aside-menu">
        <el-submenu
          index="1"
          text-color='#fff'
          active-text-color:='#ffd04b'
        >
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>导航一</span>
          </template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="1-1">选项1</el-menu-item>
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="1-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="1-4">
            <template slot="title">选项4</template>
            <el-menu-item index="1-4-1">选项1</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">导航二</span>
        </el-menu-item>
        <el-menu-item
          index="3"
          disabled
        >
          <i class="el-icon-document"></i>
          <span slot="title">导航三</span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-setting"></i>
          <span slot="title">导航四</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header
        class="s-blog-header"
        height="200px"
      >

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
