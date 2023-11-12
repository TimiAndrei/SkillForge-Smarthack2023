import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AccountPageComponent } from './components/account-page/account-page.component';
import { NgApexchartsModule } from 'ng-apexcharts';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { NgChartsModule } from 'ng2-charts';
import { Login2Component } from './components/login2/login2.component';
import { AddSkillComponent } from './components/add-skill/add-skill.component';
import { AddQuestComponent } from './components/add-quest/add-quest.component';

@NgModule({
  declarations: [
    AppComponent,
    AccountPageComponent,
    LoginComponent,
    DashboardComponent,
    Login2Component,
    AddSkillComponent,
    AddQuestComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    NgApexchartsModule,
    FormsModule,
    ReactiveFormsModule,
    NgChartsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
