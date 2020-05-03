import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-single-stock',
  templateUrl: './single-stock.component.html',
  styleUrls: ['./single-stock.component.scss']
})
export class SingleStockComponent implements OnInit {

  name: string = 'Mo vs Thani';

  price = 100.64;

  LPValue = 99.74;

  MTime: string = '4:00PM EDT';

  CValue = -7.5;

  ChangePValue = -0.65;

  VValue = 100000;

  MCValue = 1243245;

  IHValue = 101.64;

  ILValue = 98.89;

  constructor() { }

  ngOnInit(): void {
  }

}
