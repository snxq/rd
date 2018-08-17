<template>
  <div>
    <h1>RealDelicious</h1>
    <el-row>
      <el-input v-model="keyword" size="small" style="width:300px" clearable/>
      <el-button @click="search">真香</el-button>
    </el-row>
    <br/>
    <el-row>
      <img v-for="item of results" :src="item.source" :key="item" width="10%" height="200"/>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      keyword: '',
      results: []
    }
  },

  methods: {
    search: function () {
      this.axios.get(
        '/api/v1/search',
        {params: {
          keywords: this.keyword,
          limit: 20,
          offset: 0
        }}
      ).then((response) => {
        console.log(response.data)
        let data = response.data
        this.results = data
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
    /* line-height: 500px; */
    width: 50%;
  }
</style>
