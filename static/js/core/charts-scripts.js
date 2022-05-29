// // bar charts code 
// const barChartLabels = [
//     'Users',
//     'Sellers',
//     'Admins',
//   ];
//   const barChartData = {
//     labels: barChartLabels,
//     datasets: [{
//       label: 'Users Types',
//       backgroundColor: ['#FE3DD1',
//         '#B433B8',
//         '#D1DB44',],
//       borderColor: ['#FE3DD1',
//         '#B433B8',
//         '#D1DB44',],
//       data: [516, 287, 14],
//     }]
//   };

//   const barChartConfig = {
//     type: 'bar',
//     data: barChartData,
//     options: {
      
//       scales:{
//         y:{
//           grid : {
//             display :false,
//             drawTicks : false
//           },
//           display :false,
//         },
//         x:{
//           grid : {
//             display :false,
//             drawTicks : false
//           }
//         },
//       }
//     }
//   };
//   const myBarChart = new Chart(
//     document.getElementById('myBarChart'),
//     barChartConfig
//   );

//   /***************************************************/

//   //pie chart code

//   const pieChartLabels = [
//     'Accessoriy',
//     'laptobs',
//     'women clothes',
//     'men clothes ',
//     'Kids clothes',
//     'Ferntures',
//     'Hair Care',
//     'Skin Care   ',
//   ];
//   const pieChartData = {
//     labels: pieChartLabels,
//     datasets: [
//     {
//         label: 'Categories',
//         backgroundColor: [
//             '#FE3DD1',
//             '#F43DFE',
//             '#C73DFE',
//             '#BC89FF',
//             '#338EB8',
//             '#33B878',
//             '#D1DB44',
//             '#F6F33E',],
//       borderColor:[
//         '#FE3DD1',
//         '#F43DFE',
//         '#C73DFE',
//         '#BC89FF',
//         '#338EB8',
//         '#33B878',
//         '#D1DB44',
//         '#F6F33E',],
//       data: [684 ,111,516, 287, 140 ,421 ,190 ,340],
//     }]
//   };

//   const pieChartConfig = {
//     type: 'pie',
//     data: pieChartData,
//     options: {
    
//     }
//   };
//   const myPieChart = new Chart(
//     document.getElementById('myPieChart'),
//     pieChartConfig
//   );