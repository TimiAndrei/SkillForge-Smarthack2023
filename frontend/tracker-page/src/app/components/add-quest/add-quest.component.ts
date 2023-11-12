import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-quest',
  templateUrl: './add-quest.component.html',
  styleUrls: ['./add-quest.component.scss']
})
export class AddQuestComponent implements OnInit {
  questForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient, private router: Router) {
    this.questForm = this.fb.group({
      name: ['', Validators.required],
      description: [''],
      userID: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    // Add any initialization logic if needed
  }

  addQuest() {
    if (this.questForm.valid) {
      const questData = this.questForm.value;

      console.log('Sending data:', questData);

      // Send HTTP request to your backend API to add the quest
      // Adjust the URL and handle the response accordingly
      this.http.post('http://127.0.0.1:5000/api/add-quest', questData).subscribe(
        (response: any) => {
          if (response.success) {
            // Display success message
            alert(response.message);

            // Redirect or perform any other action as needed
            this.router.navigate(['/dashboard']);
          } else {
            // Display error message
            alert(`Error: ${response.error}`);
          }
        },
        (error) => {
          console.error(error);
          // Handle error, e.g., show an error message to the user
          alert('An error occurred while processing your request.');
        }
      );
    }
  }

  goToDashboard() {
    // Implement navigation logic to the dashboard or any other page
    this.router.navigate(['/dashboard']);
  }
}
