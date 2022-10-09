using UnityEngine;

public interface IBuilding
{
    void Deselect();
    void Select();
    string Name { get; }
    Vector3 Position { get; }
}