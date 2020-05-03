import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  stockname: string = '';

  constructor(private _http: HttpService, private router: Router) { }

  ngOnInit(): void {
  }

  search(): void {
    if (this._http.search(this.stockname))
      this.router.navigate(["/singlestock"]);
  }

}
