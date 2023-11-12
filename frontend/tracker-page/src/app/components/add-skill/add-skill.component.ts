import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-skill',
  templateUrl: './add-skill.component.html',
  styleUrls: ['./add-skill.component.scss']
})
export class AddSkillComponent {
  skillForm: FormGroup;

  constructor(private fb: FormBuilder, private http: HttpClient, private router: Router) {
    this.skillForm = this.fb.group({
      name: ['', Validators.required],
      category: ['', Validators.required],
      difficulty: ['', Validators.required],
      description: [''],
      deadline: [''],
      points: ['', Validators.required],
      approval: ['', Validators.required],
      questLogID: ['', Validators.required]
    });
  }

  goToDashboard() {
    this.router.navigate(['/dashboard']);
  }

  async addSkill() {
    if (this.skillForm.valid) {
      const skillData = this.skillForm.value;

      console.log('Sending data:', skillData);

      try {
        const response: any = await this.http.post('http://127.0.0.1:5000/api/addSkill', skillData).toPromise();

        if (response.success) {
          // Display success message
          alert(response.message);

          // Redirect to some success page or handle as needed
          this.router.navigate(['/dashboard']);
        } else {
          // Display error message
          alert(`Error: ${response.error}`);
        }
      } catch (error) {
        console.error(error);
        // Handle error, e.g., show an error message to the user
        alert('An error occurred while processing your request.');
      }
    }
  }
}
