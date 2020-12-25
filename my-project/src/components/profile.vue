<template>
  <div class="profile-container">
    <el-avatar :size="75" :src="image" :fit="'fill'"></el-avatar>
    <div class="personal-info">
      <div>Chen Yijin</div>
      <div>前端开发工程师</div>
    </div>
  </div>
</template>

<script>
import image from '../assets/images/avatar.png';

export default {
  name: 'profile',
  data () {
    return {
      image
    };
  }
};
</script>

<style>
.profile-container {
  position: fixed;
  transform: translate(5vw, 20vw);
  width: 150px;
  height: 200px;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  background: rgba(145, 218, 247, 0.8);
}

</style>
