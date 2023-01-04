# Proof of ultimate consistency

In general, the ultimate consistency of Omniverse Protocol is guaranteed by a deterministic cryptographic commitment mechanism and an incentive mechanism based on robocall model. The proof of the ultimate consistency is based on [Mathematical Induction](https://en.wikipedia.org/wiki/Mathematical_induction). Although this is an intuitive and non-rigorous proof, it really makes sense.  

## Proof

The core state need for the ultimate consistency is transactions including a nonce.  

### Incentive
When an Omniverse transaction happens on one chain first, the related nonce will plus 1, so the nonce on the first chain will be larger than others. After the transaction is validated according to the commitment, it is published to the public. Every synchronizer sees the new transaction and checks if any other chain has not received it, if not, they will deliver this transaction along with the commitment to the other chains. The synchronizer who submits and passes the validation first will receive rewards. There's no chance for risks or cheating as the submission will be verified by the deterministic cryptographic method, so as soon as the synchronizers discover a new legitimate transaction, they are eager to submit it for a reward.  

### Proof Steps
The transactions include transferring, minting, burning of Omniverse tokens.  

* At the first beginning, the nonce of an Omniverse account is set to be 0, every chain acts the same. Therefore $n=1$ is established.
* Suppose $n=k$ is established.
* $n=k+1$ happens when a new transaction first happens on one chain, `O20k` Parachain on Polkadot for instance. All the synchronizers will discover the new transaction on `O20k`. 
* The synchronizers will carry this transaction along with its commitment to other chains in a rush, and the first submitter will receive the rewards. 
* Very soon the state will be synchronized, and there's no need to worry about the transaction being fake as there's a cryptographic commitment with it. After executing the transaction on other chains, the balance of the related Omniverse accounts will be the same all around. Up to this point, $n=k+1$ holds.  
