<template>
  <div>
    <h1>Welcome to {{ title2 }}</h1>
    <!-- vmodel로 데이터를 투웨이!! 바인딩 -->
    <input type="text" v-model="input1" />
    <!-- onclick 대신 골뱅이클릭으로, getData 함수를 바인딩 -->
    <button type="button" @click="getData">Get</button>
    <button type="button" @click="setData">Set</button>
    <!-- 우왕 디폴드 값이 티라노로 바껴있다 -->
    <select class="form-control" v-model="region" @change="changeRegion">
      <!-- 엘리멘트 안에서 접근할때는 콜론 -->
      <option :key="idx" :value="data.k" v-for="(data, idx) in options">
        {{ data.v }}
      </option>
    </select>

    <hr />
    <!-- v-if 조건에 맞춰 보이고 안보이고 -->
    <!-- v-show = 조건을 충족을 하든 안하든 html은 랜더링은 하는데, 화면에만 보이고 안보이고 차이 -->
    <table class="table table-bordered" v-if="tableshow">
      <tr :key="i" v-for="(d, i) in options">
        <td>{{ d.k }}</td>
        <td>{{ d.v }}</td>
      </tr>
    </table>
  </div>
</template>



<script>
export default {
  // 컨트롤 하고싶은 데이터를 변수 저으이해서 씀
  data() {
    return {
      title: "개발자의 성격",
      title2: "Seoul",
      input1: "abc",
      options: [
        { k: "S", v: "vline" },
        { k: "B", v: "Busan" },
        { k: "T", v: "Tiranosaurus" },
      ],
      region: "T",
      tableshow: false,
    };
  },
  watch: {
    input1() {
      console.log(this.input1);
    },
  },
  // 모든 메쏘드
  methods: {
    getData() {
      // u can access any data from data() using 'this'!!
      alert(this.input1);
    },

    setData() {
      this.input1 = "12345";
    },

    changeRegion() {
      alert(this.region);
    },
  },
};
</script>


