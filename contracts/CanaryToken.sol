// SPDX-License-Identifier: MIT
// Contract for Canary Token
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CanaryToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("CanaryToken", "CAN") {
        _mint(msg.sender, initialSupply);
    }
}
