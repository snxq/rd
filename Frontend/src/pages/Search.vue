<template>
  <div>
    <el-row>
      <el-input v-model="keyword" size="small" width="200px" clearable/>
    </el-row>
    <el-row>
      <el-button v-on:click="search">真香</el-button>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      keyword: ''
    }
  },

  methods: {
    search: function () {
      this.axios.get(
        '',
        {params: {
          keyword: this.keyword
        }}
      ).then((response) => {
        console.log('1')
      })
    }
  }
}
</script>

<style>
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  .el-main {
    /* background-color: #E9EEF3; */
    color: #333;
    text-align: center;
    line-height: 500px;
    width: 50%;
  }
</style>
