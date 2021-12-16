Vue.component('line-chart', {
    extends: VueChartJs.Line,
    mixins: [VueChartJs.mixins.reactiveProp],
    props: ['options'],
    mounted() {
      this.renderChart(this.chartData, this.options)
    }
  })


const vm = new Vue({
    el: '#app',
    data: {
        data: new Date().toLocaleString(),
        cdata1:{
            labels: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
            datasets: [
              {
                label: 'Коммиты на GitHub',
                backgroundColor: '#f87900',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
              }
            ]
          },
    },
    methods: {
        UpdateData() {
            this.data = new Date().toLocaleString();
            console.log("anigger");
            axios
                .get('https://my-webhook-popo.herokuapp.com/get_data_chart')
//                .get('http://127.0.0.1:8000/get_data_chart')
                .then(response => (this.info = response));
//            if(this.info.data != None)
            Data = this.info.data
            this.cdata1 = Data.chart

        },
        startTimer() {
            this.interval = window.setInterval(() => {
                this.UpdateData()
            }, 1000)
        },
        mounted() {
             this.startTimer()
        },

    }
});
// });


window.addEventListener('load', function () { vm.mounted() });
