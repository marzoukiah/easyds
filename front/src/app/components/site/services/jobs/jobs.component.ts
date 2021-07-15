import { Component, OnInit } from '@angular/core';
import{ Job } from './../../../../models/job.model'
import{ JobsService } from './../../../../services/jobs.service'
import {Observable} from 'rxjs';


@Component({
  selector: 'app-jobs',
  templateUrl: './jobs.component.html',
  styleUrls: ['./jobs.component.css']
})
export class JobsComponent implements OnInit {
	jobs?:Job[];
  constructor(private jobsService:JobsService) { }

  ngOnInit(): void {
  }
  onGetAllJobs(){
  this.jobsService.getAllJobs().subscribe(data=>{
  this.jobs = data;
})
}

}
