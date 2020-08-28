Vue.component('day-view', {
    props: ['day'],
    computed: {
        rooms: function () {
            return this.$store.state.rooms
        },
        events: function () {
            return this.$store.state.events
        }
    },
    template: '#day-view',
    methods: {
        show: () => {
            $('.ui.modal')
                .modal('show')
            ;
        }
    }

})
const store = new Vuex.Store({
    state: {
        title: "Hello Title",
        rooms: [],
        events: {},
    }
})
const vm = new Vue({
    el: '#app',
    store,
    data: {
        message: '页面加载于 ' + new Date().toLocaleString(),
        calendar: [
            [{
                number: 1,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, 11, null, null, null, null, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 2,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 3,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 4,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 5,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 6,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 7,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }],
            [{
                number: 8,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 9,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 10,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 11,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 12,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 13,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }, {
                number: 14,
                events: {
                    10: [null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],
                    11: [null, null, null, null, null, null, null, null, 11, 11, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null]
                }
            }]
        ]
    },
    methods: {
        convert: function () {
            axios.get("api/room").then(res => {
                this.$store.state.rooms = res.data.items;
            }).catch(function (error) {
                console.error(error);
            });
            axios.get("api/event").then(res => {
                var map = {};
                for (var index in res.data.items) {
                    map[res.data.items[index].key] = res.data.items[index];
                }
                this.$store.state.events = map;
            }).catch(function (error) {
                console.error(error);
            });
        }
    },
    created() {
        this.convert();
    },
    mounted() {
        console.log(this);
        console.log(this.$store);
        console.log(this.$store.state);
        console.log(this.$store.state.title);
    }
});
window.vm = vm;