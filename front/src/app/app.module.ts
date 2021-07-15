import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/layout/header/header.component';
import { SidemenuComponent } from './components/layout/sidemenu/sidemenu.component';
import { FooterComponent } from './components/layout/footer/footer.component';
import { HomeComponent } from './components/site/home/home.component';
import { JobsComponent } from './components/site/services/jobs/jobs.component';
import { HttpClientModule } from '@angular/common/http';
import { JobItemComponent } from './components/site/services/job-item/job-item.component';

const appRoutes: Routes = [
{path:'home', component: HomeComponent},
{path:'services/jobs', component: JobsComponent},
{path:'services/job-item/:jobId', component: JobItemComponent},
{path: '', redirectTo:'/home', pathMatch:'full'}
];



@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    SidemenuComponent,
    FooterComponent,
    HomeComponent,
    JobsComponent,
    JobItemComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
