import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-single-stock',
  templateUrl: './single-stock.component.html',
  styleUrls: ['./single-stock.component.scss']
})
export class SingleStockComponent implements OnInit {

  stockname: string = 'Mo vs Thani';

  price = 100.64;

  LPValue = 99.74;

  MTime: string = '4:00PM EDT';

  CValue = -7.5;

  ChangePValue = -0.65;

  VValue = 100000;

  MCValue = 1243245;

  IHValue = 101.64;

  ILValue = 98.89;

  constructor(private _http: HttpService, private router: Router) { }

  ngOnInit(): void {
  }

  search() {
    if (this._http.search(this.stockname))
      this.router.navigate(["/singlestock"]);
  }

}
