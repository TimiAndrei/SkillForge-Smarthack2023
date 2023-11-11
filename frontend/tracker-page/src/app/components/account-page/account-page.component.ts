import { Component, ViewChild } from '@angular/core';


@Component({
  selector: 'app-account-page',
  templateUrl: './account-page.component.html',
  styleUrls: ['./account-page.component.scss']
})
export class AccountPageComponent {
  

  name: string = 'John Doe';
  level: number = 1;
  picture: string = 'https://i.pravatar.cc/300';


  
}




