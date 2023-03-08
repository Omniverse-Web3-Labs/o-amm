# Proof of ultimate consistency

In general, the ultimate consistency of Omniverse Protocol is guaranteed by a deterministic cryptographic commitment mechanism and an incentive mechanism based on robocall model. The proof of the ultimate consistency is based on [Mathematical Induction](https://en.wikipedia.org/wiki/Mathematical_induction). Although this is an intuitive and non-rigorous proof, it really makes sense.  

## Proof

The core state need for the ultimate consistency is transactions including a nonce.  

### Incentive
When an Omniverse transaction happens on one chain first, the related nonce will plus 1, so the nonce on the first chain will be larger than others. After the transaction is validated according to the commitment, it is published to the public. Every synchronizer sees the new transaction and checks if any other chain has not received it, if not, they will deliver this transaction along with the commitment to the other chains. The synchronizer who submits and passes the validation first will receive rewards. There's no chance for risks or cheating as the submission will be verified by the deterministic cryptographic method, so as soon as the synchronizers discover a new legitimate transaction, they are eager to submit it for a reward.  

### Proof Steps
Take transferring ERC6358 Fungible Tokens for example. A non-rigorous but intuitive proof is as below:  

- At the first beginning, the nonce of `o-accounts` are set to be 0, every chain acts the same. Therefore $n=0$ is established.
- Suppose $n=k$ is established.
- $n=k+1$ happens when a new `o-transaction` first appears on one chain, Etheruem for instance. All the synchronizers will discover the new `o-transaction` on ERC6358 smart contracts on Etheruem. 
- The synchronizers will carry this `o-transaction` along with its signature to other chains for rewards.
- Very soon the state will be synchronized, and there's no need to worry about the `o-transaction` being fake as there's a signature with it. After executing the `o-transaction` on all chains, the balance and the nonce of the related Omniverse accounts will be the same all around. Up to this point, $n=k+1$ holds.  
