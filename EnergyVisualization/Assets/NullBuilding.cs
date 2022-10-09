using UnityEngine;

public sealed class NullBuilding : IBuilding
{
    private static readonly NullBuilding instance = new NullBuilding();

    // Explicit static constructor to tell C# compiler
    // not to mark type as beforefieldinit
    static NullBuilding() { }

    private NullBuilding() { }

    public static NullBuilding Instance
    {
        get
        {
            return instance;
        }
    }

    public string Name => "";

    public Vector3 Position => Vector3.zero;

    public void Deselect() { }
    public void Select() { }
}