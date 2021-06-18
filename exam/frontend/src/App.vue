<template>
  <div id="app">
    <img src="../public/school.png">
    <p id="title">
      <router-link to="/">오늘의 급식</router-link>
    </p>
    <router-view></router-view>
  </div>
</template>

<style lang="scss">
  #title{
    text-align: center;
    background: linear-gradient(to right, #A7A3FF,#FFA7A3, #671cc4, #5673bd); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    height: 100px;
    font-size: 60pt;
  }

  img {
    position: relative;
    left: 42.5%;
    width: 15%;
    height: 15%;
  }
</style>