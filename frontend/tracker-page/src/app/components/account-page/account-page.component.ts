import { RouterModule, Routes, Router } from '@angular/router';
import { ChartType } from 'chart.js';
import { Component, ViewChild, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-account-page',
  templateUrl: './account-page.component.html',
  styleUrls: ['./account-page.component.scss']

})


export class AccountPageComponent implements OnInit {

  apiURL = 'http://127.0.0.1:5000/api/test';
  responseData: any;

  name: string = 'John Doe';
  level: number = 1;
  picture: string = 'https://i.pravatar.cc/300';



  simpleTasks: number = 5;
  mediumTasks: number = 2;
  hardTasks: number = 1;

  radarChartOptions = {
    responsive: true,
    scale: {
      ticks: {
        display: false
      }
    },
    legend: {
      display: false // Set this to false to hide the legend
    }
  };
  radarChartLabels = ['Coding', 'Reading', 'Cooking', 'Guitar', 'French'];

  radarChartData = [
    {
      data: [100, 70, 20, 50, 75],
      label: '',
      borderColor: '#3cba9f',
      backgroundColor: 'rgba(60,186,159,0.5)',
    },
  ];

  radarChartType: ChartType = 'radar';

  constructor(private http: HttpClient, private router: Router) { }

  errorMessage: string = '';



  userName: string = '';

  ngOnInit(): void {
    // this.http.get(this.apiURL)
    //   .subscribe((data: any) => {
    //     this.responseData = data;
    //     console.log(this.responseData);
    //   });


    this.http.get('http://127.0.0.1:5000/api/get-user').subscribe((data: any) => {

      this.userName = data.currentUser.email;

      console.log(data);

    })

    this.http.get('http://127.0.0.1:5000/api/get-quote').subscribe(
      (data: any) => {
        // Handle successful response
        console.log('Data received:', data);
      },
      (error: any) => {
        // Handle error
        this.errorMessage = error.error.text;

        //strip the final part, after the last point
        this.errorMessage = this.errorMessage.substring(0, this.errorMessage.lastIndexOf('.'));

        console.log(this.errorMessage);

        // You can add more specific error handling logic here
      }
    );

  }

  goToDashboard() {
    this.router.navigate(['/dashboard']);
  }

  logout() {
    // Redirect to login page
    this.router.navigate(['/login']);

    // Send request to Flask API to clear current user
    this.http.post('http://127.0.0.1:5000/api/logout', {}).subscribe(response => {
      console.log(response);  // Log the API response
    });
  }

}


