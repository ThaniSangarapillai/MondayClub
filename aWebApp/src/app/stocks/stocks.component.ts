import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-stocks',
  templateUrl: './stocks.component.html',
  styleUrls: ['./stocks.component.scss']
})
export class StocksComponent implements OnInit {

  constructor(private _http: HttpService, private router: Router) { }

  ngOnInit(): void {
    this.getstocks();
  }

  getstocks(): void {
    console.log("hello");
    this._http.getstocks();
  }

}
