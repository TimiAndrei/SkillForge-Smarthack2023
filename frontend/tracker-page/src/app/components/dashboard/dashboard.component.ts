import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent {

  constructor(private router: Router) { }

  picture: string = 'https://i.pravatar.cc/300';



  goToAccount() {
    this.router.navigate(['/account']);
  }

}
