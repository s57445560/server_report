<template>
<el-container>
  <el-header style="background-color: #409EFF;">
          <el-row >
            <el-col :span="5">
                <h2 style="color: white;font-family: Microsoft YaHei;margin-top: 15px;" align="left">
                    <i class="el-icon-menu"></i>
                    服务器资源报表
                </h2>
            </el-col>
        </el-row>


  </el-header>
  <el-container>
    <el-aside width="200px">
      <Aside></Aside>
    </el-aside>
    <el-main style="padding-left: 2px" align="left">
      <router-view/>
    </el-main>
  </el-container>
</el-container>

</template>

<script>
  import Aside from '@/components/Aside'
  import Report from '@/components/report'
  export default {
    name: 'HelloWorld',
    data () {
      return {
        msg: 'home',
      }
    },
    methods: {
         reload () {
             this.isRouterAlive = false;
             this.$nextTick(() => (this.isRouterAlive = true))
           }
      },
    computed:{

        },
    created(){
            // this.$store.dispatch('base_list');
        },
    components: {
            Aside,
            Report,
        }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .el-aside {
    color: #333;
  }
</style>
