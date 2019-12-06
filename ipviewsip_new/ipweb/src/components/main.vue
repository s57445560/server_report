<template>
  <div id="main">
    <el-row :gutter="12">
      <el-col :span="6">
        <el-card shadow="always">
          <i class="el-icon-s-platform"></i>服务器总数量：{{get_home_s.ip_all}}
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="always">
          <i class="el-icon-s-platform"></i>环境总数量：{{get_home_s.e_all}}
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="always">
          <i class="el-icon-s-platform"></i>物理机总数量：{{get_home_s.p_all}}
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="always">
          <i class="el-icon-s-platform"></i>虚拟机总数量：{{get_home_s.v_all}}
        </el-card>
      </el-col>
    </el-row>
    <div id="container" style="height: 400px;padding-top: 8px;"></div>
  </div>
</template>

<script>
  export default {
    name: 'Main',
    data () {
      return {
        msg: '主页面'
      }
    },
    computed:{
      get_home_s(){
        return this.$store.state.Base.Home;
      }
    },
    methods:{
    },
    created(){
      console.log(this.baseConfig.request_url,"111111111111111");
      this.$store.dispatch("get_home");
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
