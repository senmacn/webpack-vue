<template>
  <el-main>
    <img src="@/assets/logo.png" />
    <div class="C-home">我的项目</div>
    <el-button
      type="primary"
      @click.prevent
    >
      <router-link to="blog">我的博客</router-link>
    </el-button>
  </el-main>
</template>

<script>
export default {
  name: 'CHome'
};
</script>
