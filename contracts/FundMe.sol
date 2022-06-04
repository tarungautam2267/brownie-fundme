//SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract FundMe{
    mapping(address=>uint256) public addressToAmountMapping;
    address[] funders; 
    address public owner;
    AggregatorV3Interface public pricefeed;

    modifier onlyOwner(){
        require(msg.sender==owner);
        _;
    }

    constructor(address _pricefeed) public{
        pricefeed = AggregatorV3Interface(_pricefeed);
        owner=msg.sender;
    }
    function fund() public payable{
        uint256 minimumUsd = 50*10**18;
        require(getconversionrate(msg.value)>=minimumUsd, "Not Enough");
        addressToAmountMapping[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getEntrancefee() public view returns(uint256){
        uint256 minimumUSD = 50*10**18;
        uint256 price = getprice();
        uint256 precision = 1*10**18;
        return (minimumUSD*precision)/price;
    }

    function getversion() public view returns(uint256){
        return pricefeed.version();
    }

    function getprice() public view returns(uint256){
        (,int256 answer,,,)=pricefeed.latestRoundData();
        return uint256(answer*10000000000);
    }

    function getconversionrate(uint256 _amount) public view returns(uint256){
        uint256 ethprice = getprice();
        uint256 tousd = (_amount*ethprice)/1000000000000000000;
        return tousd;
    }

    function withdraw() payable onlyOwner public{
        payable(msg.sender).transfer(address(this).balance);
        for(uint256 i=0; i<funders.length; i++){
            address funder = funders[i];
            addressToAmountMapping[funder]=0;
        }
        funders = new address[](0);
    }

    function getdecimals() public view returns(uint256){
        AggregatorV3Interface deci= AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return deci.decimals();
    }

}