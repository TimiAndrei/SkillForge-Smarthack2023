import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AccountPageComponent } from './components/account-page/account-page.component';
import { LoginComponent } from './components/login/login.component';
import { Login2Component } from './components/login2/login2.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { AddSkillComponent } from './components/add-skill/add-skill.component';
import { AddQuestComponent } from './components/add-quest/add-quest.component';

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'account', component: AccountPageComponent },
  { path: 'login2', component: Login2Component },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'addSkill', component: AddSkillComponent },
  { path: 'addQuest', component: AddQuestComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
