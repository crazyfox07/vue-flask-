<template>
  <div id="app">
    <el-container>
      <el-container>
        <el-header >
            <el-row>
              <el-col :span="24"><div  class="grid-content">IP代理</div></el-col>
           </el-row>
        </el-header>
        <el-main><router-view/></el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.el-row {
  margin-bottom: 200px;
  last-child {
   margin-bottom: 0;
 }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;

  background: #000000;
  color:#FFFFFF;
  text-align:left;
  line-height:50px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
